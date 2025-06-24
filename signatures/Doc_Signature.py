from dspy import Input, Output, dspy

class Doc_Signature(dspy.Signature):
    """
    A class to define the signature for document processing tasks.
    """

    input_text: str =Input()
    
    output: str= Output(
        description="The processed output of the document.",
        example="This is an example of processed document text."
    )

