# you can check sms-classifier here
https://email-sms-spam-tryit.streamlit.app/?embed_options=dark_theme,show_footer
# Naive Bayes Spam Classifier

This project implements a spam classifier using the Naive Bayes algorithm to detect spam in emails and SMS messages.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [Performance](#performance)
- [Contributing](#contributing)
- [License](#license)

## Overview

This spam classifier uses the Naive Bayes algorithm to differentiate between spam and legitimate messages (ham). It can be applied to both email and SMS contexts, providing a versatile tool for filtering unwanted communications.

## Features

- Classifies messages as spam or ham
- Supports both email and SMS message formats
- Uses Naive Bayes algorithm for efficient and accurate classification
- Easy-to-use command-line interface
- Configurable training and testing options

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/naive-bayes-spam-classifier.git
   cd naive-bayes-spam-classifier
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To classify a message, use the following command:

```
python classify.py "Your message here"
```

For batch classification of messages in a file:

```
python classify_batch.py path/to/your/messages.txt
```

## Dataset

The classifier is trained on the [SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection). This dataset contains 5,574 SMS messages that have been labeled as either spam or ham.

## Model

The Naive Bayes classifier uses the following features:
- Word frequency
- Character n-grams
- Message length
- Presence of special characters

## Performance

On our test set, the classifier achieves:
- Accuracy: 96.5%
- Precision: 100.0%
- Recall: 94.3%
- F1 Score: 96.0%

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
