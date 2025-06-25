from dspy import InputField, OutputField, dspy

class Doc_Signature(dspy.Signature):
    """
    A class to define the signature for document processing tasks.
    """

    input_text: str =InputField()
    
    output: str= OutputField(
        description="Generate a summary of the document, focusing on the main themes, characters, and events."
    )



