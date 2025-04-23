"""
@Author				: XiaoTao
@Email				: 18773993654@163.com
@Lost modifid		: 2023/4/28 16:49
@Filename			: num_tokens.py
@Description		: 
@Software           : PyCharm
"""
import tiktoken as tiktoken

from utils.str_utils import key_from_dicts

model_name = "gpt-3.5-turbo-0613"


def num_tokens_from_messages(messages, model=model_name):
    """Returns the number of tokens used by a list of messages."""
    messages = key_from_dicts(messages)
    try:
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        if model == model_name:  # note: future models may deviate from this
            num_tokens = 0
            for message in messages:
                num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":  # if there's a name, the role is omitted
                        num_tokens += -1  # role is always required and always 1 token
            num_tokens += 2  # every reply is primed with <im_start>assistant
            return num_tokens
        else:
            raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
        See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
    except Exception as e:
        return 100


def split_messages(messages, token_limit=2048, model=model_name):
    current_split = []
    current_tokens = 0

    for message in messages[::-1]:
        message_tokens = num_tokens_from_messages([message], model)
        if current_tokens + message_tokens <= token_limit:
            current_split.append(message)
            current_tokens += message_tokens
        else:
            break
    if len(current_split) % 2 == 0 and len(current_split) > 1:
        current_split.pop()
    return current_split[::-1]
