from openai import OpenAI

class chatgpt_example:
    transactions = None

    def __init(self, input_value):
        self.transactions = input_value
                    
    def summarize_assistant(self, first_name, last_name):
        print("testing")

        client = OpenAI()
        transString = ""
        for tran in self.transactions:
            transString += (f"(transaction: {tran['amount']}, description: {tran['desc']}, Date:{tran['datetrans']})")
        chat_content = f"(first_name: {first_name}, last_name: {last_name}), [{transString}]"
        completion = client.chat.completions.create(

            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a chat Assistant for financial bank system. Please respond as a telephone assistant with transaction details."},
                {
                    "role": "user",
                    "content": chat_content
                }
            ]
        )


        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

input_trans = [{"amount":20, "desc": "coffee", "datetrans": "02-02-2025"},
                        {"amount":10, "desc": "movie", "datetrans": "02-01-2025"}]

test = chatgpt_example(input_trans)
test.summarize_assistant("gopi", "test")

#summarize_assistant("gopi", "test", transactions)