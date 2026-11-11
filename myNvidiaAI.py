# this script use for reading text,color etc. from Image
import os
from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "<Your API KEY>"
)

inputtext ="who is India PM ?"
mymodel = "nvidia/nemotron-3-ultra-550b-a55b"  
#"nvidia/nemotron-3.5-super-vl-120b-a12b"

completion = client.chat.completions.create(
  model=mymodel,
  messages=[{"role": "user", "content": 
             [{"type": "text", "text": inputtext},]
           }],
  temperature=1,
  top_p=0.95,
  max_tokens=16384,
  parallel_tool_calls=True,
  seed=42,
  extra_body={"chat_template_kwargs": {"enable_thinking": True}},
  stream=True
)
# completion = client.chat.completions.create(
#   model="nvidia/nemotron-3.5-super-vl-120b-a12b",
#   messages=[{"role": "user", "content": 
#              [{"type": "text", "text": "Read the traffic sign in this image. What does it say, and what color is the sign?"}, 
#               {"type": "image_url", "image_url": {"url": "https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1a.jpg"}
#                }]
#              }],
#   temperature=1,
#   top_p=0.95,
#   max_tokens=16384,
#   parallel_tool_calls=True,
#   seed=42,
#   extra_body={"chat_template_kwargs": {"enable_thinking": True}},
#   stream=True
# )

for chunk in completion:
  if not chunk.choices:
    continue
  reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
  if reasoning:
    print(reasoning, end="")
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
