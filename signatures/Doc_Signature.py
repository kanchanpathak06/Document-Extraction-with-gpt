from dspy import InputField, OutputField, dspy

class Doc_Signature(dspy.Signature):
    """
    A class to define the signature for document processing tasks.
    """

    input_text: str =InputField()
    
    output: str= OutputField(
        description="The processed output of the document."
    )

