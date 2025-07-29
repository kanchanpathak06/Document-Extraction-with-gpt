# Document-Extraction-with-Dspy

## Overview

This project demonstrates how to use [dspy](https://github.com/stanfordnlp/dspy) for efficient and accurate text extraction from documents using GPT-based models. dspy is a powerful library that simplifies prompt engineering, chaining, and orchestration of large language models (LLMs) for various NLP tasks.

## Why Use dspy for Text Extraction?

- **Simplicity:** dspy provides an intuitive interface to define extraction tasks, reducing boilerplate code and making it easy to experiment with different prompts and models.
- **Modularity:** You can easily compose and reuse extraction chains, making your codebase cleaner and more maintainable.
- **Prompt Optimization:** dspy supports prompt tuning and optimization, helping you achieve higher accuracy in extracting relevant information.
- **Integration:** Works seamlessly with popular LLMs, including OpenAI's GPT models, allowing you to leverage state-of-the-art language understanding.
- **Rapid Prototyping:** Quickly build and iterate on extraction pipelines without deep knowledge of NLP or prompt engineering.

## Example Use Cases

- Extracting key information (names, dates, addresses) from legal or financial documents.
- Summarizing long documents or extracting specific sections.
- Automating data entry by pulling structured data from unstructured text.

## Getting Started

1. **Install dspy:**
   ```bash
   pip install dspy

2. Basic Usage Example
```python
import dspy

# Define your extraction prompt
prompt = "Extract all email addresses from the following text: {document}"

# Use dspy to run the prompt with your document
result = dspy.run(prompt, document="Contact us at info@example.com or support@example.org.")

print(result)
# Output: ['info@example.com', 'support@example.org']

3. Customize and Extend:

Chain multiple extraction steps.
Integrate with other tools for post-processing.
Conclusion
Using dspy for document extraction with GPT models streamlines the process, improves accuracy, and accelerates development. It is a valuable tool for anyone working with unstructured text data.

For more details, see the dspy documentation.