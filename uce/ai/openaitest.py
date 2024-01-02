from pydantic import BaseModel
import openai

class Document(BaseModel):
    prompt: str

def inference(prompt: str) -> list:
    openai.api_key = ' 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'
    openai.organization = 'org-SZnLAEygLCSs1V7clZ4dCPdu'

    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Convierte la siguiente frase a binario: {prompt}",
        max_tokens=50
    )

    inference_result = completion.choices[0].text
    usage_info = completion.usage.total_tokens

    return [inference_result, usage_info]
