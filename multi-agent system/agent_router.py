from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def routing_prompt(llm_name, options, members):
    system_prompt = get_system_prompt(llm_name)

    if llm_name == 'gemini':
        prompt = ChatPromptTemplate.from_messages(
            [("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            (
                "system",  
                "Given the conversation above, who should act next? Or is the task complete and should we FINISH?  Select one of: {options}"
            )]).partial(options=str(options), members=", ".join(members))
    
    return prompt

def get_system_prompt(llm_name):
    if llm_name == 'gemini':
        SYSTEM_PROMPT = llama3_begin_template + (
            "You are a supervisor agent tasked with managing a conversation between the following workers:  {members}. "
            "User has uploaded a CV and sent a query. Given the uploaded CV and following user request, respond with the worker to act next. "
            "Each worker will perform a task and respond with their results and status. "
            "After the result: ask yourself if the original query is satisfied. If not, route to the next appropriate task. "
            "When the task is finished, respond with FINISH."
        ) + llama3_end_template
    
    return SYSTEM_PROMPT
