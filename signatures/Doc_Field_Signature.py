from dspy import InputField, OutputField, dspy

class Doc_Field_Signature(dspy.Signature):
    """
    A class to define the signature for document processing tasks.
    """

    input_text: str =InputField()
    
    gregor_transformation: str= OutputField(
        description="What unusual transformation does Gregor Samsa experience? "
    )

    gregor_job: str = OutputField(
        description="What was Gregor Samsa's job before he transformed into a bug?"
    )

    

