import os
import argparse
from call_function import available_functions, call_function
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
	raise RuntimeError("Couldn't fetch API key, check environment")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
	print("Hello from aiagent!")
	
	response = client.models.generate_content(
		model='gemini-2.5-flash',
		contents=messages,
		config=types.GenerateContentConfig(
			system_instruction=system_prompt,
			tools=[available_functions],
		),
	)
	if not response.usage_metadata:
		raise RuntimeError("No response... maybe it's sleeping?")
	if response.function_calls:
		for function in response.function_calls:
			try:
				func_result =  call_function(function, args.verbose)
			except Exception as e:
				print(f"There was a {e} type problem while calling {function}")
				continue
			if not func_result.parts or not func_result.parts[0].function_response or not func_result.parts[0].function_response.response:
				raise Exception(f"There's been a problem with the function call, try debugging.")
			print(f"-> {func_result.parts[0].function_response.response}")
	else:
		if args.verbose:
			print(f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}\nResponse:\n{response.text}")
		else:
			print(response.text)

if __name__ == "__main__":
	main()
