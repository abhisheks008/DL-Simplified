# Dataset

## Description

This project uses a collection of QR code images, split into benign and malicious sets. Each QR code image is decoded to extract its embedded URL, which is then used to build a labeled text dataset for classification.

---

## Dataset Information

- QR code images organized into `benign` and `malicious` folders
- URLs decoded from each QR code using image decoding
- Two target classes: benign (0) and malicious (1)
- Duplicate URLs checked and reported
- Suitable for binary text classification

---

## Dataset File

Decoded URLs are exported to:

decoded_urls.csv


with columns `url` and `label`.

---

## Applications

- Malicious QR Code Detection
- Phishing Link Screening
- Mobile/Web Security Analytics

---

## Acknowledgement

Special thanks to the dataset creator for making the QR code image collection available for educational and research purposes.