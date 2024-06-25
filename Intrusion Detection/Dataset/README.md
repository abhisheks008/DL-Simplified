
---

# KDD Cup 1999 Dataset

## Overview

The KDD Cup 1999 dataset is a benchmark dataset commonly used for evaluating intrusion detection systems (IDS). It was introduced as part of the Third International Knowledge Discovery and Data Mining Tools Competition, held alongside the Fifth International Conference on Knowledge Discovery and Data Mining (KDD-99).

## Description

The dataset comprises network connection records captured in a university department's local area network (LAN) over a period of several weeks. It is structured to represent various types of network traffic, including normal and malicious activities. Multiple types of attacks were simulated in the dataset, covering denial of service (DoS), user to root (U2R), remote to local (R2L), and probe attacks.

## Files

- **[kddcup.data_10_percent.gz](https://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz)**: This compressed file contains a 10% subset of the complete dataset. It serves as a manageable sample for initial exploration and experimentation.

## Columns

The dataset is composed of numerous features describing each network connection record. Some of the key columns include:

- `duration`: The length of the connection in seconds.
- `protocol_type`: The protocol used in the connection (e.g., TCP, UDP, ICMP).
- `service`: The network service on the destination (e.g., http, smtp, telnet).
- `flag`: The status of the connection (e.g., SF for normal, S0 for connection attempts, REJ for rejected connections).
- `src_bytes`: The number of data bytes from source to destination.
- `dst_bytes`: The number of data bytes from destination to source.
- `target`: Binary label indicating whether the connection is normal or an attack.
- `Attack Type`: Categorical label specifying the type of attack (DoS, U2R, R2L, probe).

## Usage

The KDD Cup 1999 dataset serves as valuable data for training and evaluating intrusion detection systems (IDS), anomaly detection algorithms, and machine learning models in general. Researchers and practitioners in the field of cybersecurity often utilize this dataset to benchmark their approaches and compare performance against existing methods.
