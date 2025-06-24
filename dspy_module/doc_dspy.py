from dspy import dspy
from signatures.Doc_Signature import Doc_Signature


lm=dspy.LM(
    model="azure/gpt-40",
    api_key="your_api_key_here",  # Replace with your actual API key
    api_base="https://your_api_base_here",  # Replace with your actual API base
    cache=False,
    num_retries=3,
    logprobs=True,
    top_logprobs=5,
)

dspy.confiure(lm=lm)

class dspy_doc:
    """
    A class to handle document processing using dspy.
    """

    def __init__(self):
        super().__init__()
        self.classifier= dspy.Predict(signature=Doc_Signature)

    def forward(self,text):
        result=self.classifier(inout_text=text)
        return result