from dotenv import load_dotenv
import os
from openai import OpenAI
import google.generativeai as genai
from loguru import logger
from PyPDF2 import PdfReader

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

class InitiateModel:
    def __init__(self, model_type: str):
        self.model_type = model_type

    def get_model(self):
        if self.model_type == "openai":
            model = OpenAI(api_key=OPENAI_API_KEY)            
            return model
        else:
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            return model

class HireView:
    @staticmethod
    def extract_pdf_text(pdf_file):
        try:
            reader = PdfReader(pdf_file)
            pages = reader.pages
            text = " ".join([page.extract_text() for page in pages])
            return text
        except Exception as e:
            logger.error(f"Error reading PDF file: {e}")
            return None

    @staticmethod
    def get_model_response(model_type: str, prefix: str, pdf_text: str, job_description: str):
        try:
            logger.info(f"Initialize model: {model_type}...")
            model = InitiateModel(model_type).get_model()
        except Exception as e:
            logger.error(f"Error initializing model: {e}")
            return None

        try:
            prompt = prefix + pdf_text + job_description
            if model_type == "openai":
                completion = model.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.5,
                )

                response = completion.choices[0].message.content
                return response
            else:
                response = model.generate_content(prompt)
                return response
        except Exception as e:
            logger.error(f"Error getting model response: {e}")
            return None