import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ai_model import model_run

res = model_run.predict("바보멍청이")
print(res)