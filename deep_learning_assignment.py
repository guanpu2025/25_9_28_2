import os
import pandas as pd
from PIL import Image

import torch
from torch.utils.data import Dataset
from torchvision import transforms

import torch.nn as nn
import torchvision.models as models

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
import torch.nn.functional as F
from torch.utils.data import DataLoader
from transformers import BertModel
from transformers import BertTokenizer

class FoodDataset(Dataset):
    def __init__(self, root_dir, csv_file, tokenizer, transform=None):
        self.root_dir = root_dir
        self.data = pd.read_csv(csv_file)
        self.transform = transform
        self.tokenizer = tokenizer

        self.label2idx = {
            "french_fries": 0,
            "youtiao": 1,
            "baozi": 2,
            "rice": 3,
            "cupcake": 4
        }

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]

        # image
        img_path = os.path.join(self.root_dir, row["image_path"])
        image = Image.open(img_path).convert("RGB")
        if self.transform:
            image = self.transform(image)

        # text
        text = row["text"]
        text = self.tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=32,
            return_tensors="pt"
        )

        # label
        label = self.label2idx[row["label"]]

        return image, text["input_ids"].squeeze(0), text["attention_mask"].squeeze(0), label

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

tokenizer = BertTokenizer.from_pretrained("D:/.vscode/deep_learning/课程设计/bert-base-chinese")

train_dataset = FoodDataset(
    root_dir="D:/.vscode/deep_learning/课程设计/Food_Multimodal/train/images",
    csv_file="D:/.vscode/deep_learning/课程设计/Food_Multimodal/train/metadata.csv",
    tokenizer=tokenizer,
    transform=transform
)

val_dataset = FoodDataset(
    root_dir="D:/.vscode/deep_learning/课程设计/Food_Multimodal/val/images",
    csv_file="D:/.vscode/deep_learning/课程设计/Food_Multimodal/val/metadata.csv",
    tokenizer=tokenizer,
    transform=transform
)

test_dataset = FoodDataset(
    root_dir="D:/.vscode/deep_learning/课程设计/Food_Multimodal/test/images",
    csv_file="D:/.vscode/deep_learning/课程设计/Food_Multimodal/test/metadata.csv",
    tokenizer=tokenizer,
    transform=transform
)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

#for images, labels in train_loader:
#    print(images.shape)  # [32, 3, 224, 224]
#    print(labels.shape)  # [32]
#   break

class MultiModalModel(nn.Module):
    def __init__(self):
        super().__init__()

        # image encoder
        self.cnn = models.resnet18(pretrained=True)
        self.cnn.fc = nn.Linear(self.cnn.fc.in_features, 256)

        # text encoder
        self.bert = BertModel.from_pretrained("D:/.vscode/deep_learning/课程设计/bert-base-chinese")
        self.text_fc = nn.Linear(768, 256)

        # fusion classifier
        self.classifier = nn.Sequential(
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Linear(128, 5)
        )

    def forward(self, image, input_ids, attention_mask):

        img_feat = self.cnn(image)  # [B,256]

        text_out = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        ).pooler_output  # [B,768]

        text_feat = self.text_fc(text_out)  # [B,256]

        fused = torch.cat([img_feat, text_feat], dim=1)  # [B,512]

        out = self.classifier(fused)

        return out
    
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = MultiModalModel().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

train_losses = []
val_accs = []

for epoch in range(5):

    model.train()
    total_loss = 0

    for images, input_ids, attention_mask, labels in train_loader:

        images = images.to(device)
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)
        labels = labels.to(device)

        outputs = model(images, input_ids, attention_mask)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    train_losses.append(avg_loss)
    print(f"Epoch {epoch+1}, Train Loss: {avg_loss:.4f}")

    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for images, input_ids, attention_mask, labels in val_loader:

            images = images.to(device)
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)

            outputs = model(images, input_ids, attention_mask)
            _, preds = torch.max(outputs, 1)

            correct += (preds == labels).sum().item()
            total += labels.size(0)

    acc = correct / total
    val_accs.append(acc)
    print("Val Acc:", acc)

test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

model.eval()

correct = 0
total = 0
all_preds = []
all_labels = []

with torch.no_grad():
    for images, input_ids, attention_mask, labels in test_loader:

        images = images.to(device)
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)
        labels = labels.to(device)

        outputs = model(images, input_ids, attention_mask)
        _, preds = torch.max(outputs, 1)

        correct += (preds == labels).sum().item()
        total += labels.size(0)

        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

test_acc = correct / total
print("Test Acc:", test_acc)

torch.save(model.state_dict(), "best_model.pth")

plt.figure()

plt.subplot(1, 2, 1)
plt.plot(train_losses)
plt.title("Train Loss")

plt.subplot(1, 2, 2)
plt.plot(val_accs)
plt.title("Val Accuracy")

plt.show()

with torch.no_grad():
    for images, input_ids, attention_mask, labels in test_loader:

        images = images.to(device)
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)
        labels = labels.to(device)

        outputs = model(images, input_ids, attention_mask)
        _, preds = torch.max(outputs, 1)

cm = confusion_matrix(all_labels, all_preds)

plt.figure(figsize=(6,5))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=["fries","youtiao","baozi","rice","cupcake"],
    yticklabels=["fries","youtiao","baozi","rice","cupcake"]
)
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.show()