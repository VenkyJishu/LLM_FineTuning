import json
import os
from openai import AzureOpenAI

print(os.listdir("Dataset"))


class DataIngestion():
    def __init__(self):
        self.input_file = os.path.join("Dataset","log.txt")
        self.output_file = "log_finetue.jsonl"
        self.openai_client = AzureOpenAI(
            api_key="your-azure-api-key", 
            api_version="2023-12-01-preview",
            azure_endpoint="https://<your-resource-name>.openai.azure.com"
        )
    def summarize_log(self,log_text):
        
        response = self.openai_client.chat.completions.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are an expert summarizer of Azure cloud logs."},
                {"role": "user", "content": f"Summarize this log:\n{log_text}"}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    def gen_jsonl_file(self):
        with open(self.input_file,'r') as in_file , open(self.output_file,'w') as out_file:
            for line in in_file:
                line = line.strip()
                if not line:
                    continue; # Skip empty lines

                instruction = "Summarize the Azure log"
                system_msg = {'role':'system','content': 'You are expert log summarizer'}
                user_msg = {'role':'user','content':f"{instruction}\n{line}"}

                summary = self.summarize_log(line)
                assistant_msg = {'role':'assistant','content':summary}

                jsonl_obj = {"messages":[system_msg,user_msg,assistant_msg]}
                out_file.write(json.dumps(jsonl_obj) + "\n")

if __name__ == "__main__":
    di =  DataIngestion()
    di.gen_jsonl_file()
