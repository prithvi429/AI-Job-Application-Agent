llama3_begin_template = "<|begin_of_text|><|start_header_id|>system<|end_header_id|> "
llama3_end_template = " <|eot_id|> <|start_header_id>assistant<|end_header_id|>"

def get_system_prompt():
    """
    This function generates the system prompt for Gemini.
    The system prompt describes the role of the supervisor agent managing tasks for other agents.
    """
    SYSTEM_PROMPT = llama3_begin_template + (
        "You are a supervisor agent tasked with managing a conversation between the "
        "following workers:  {members}. User has uploaded a document and sent a query. Given the uploaded document and following user request, "
        "respond with the worker to act next. Each worker will perform a task and respond with their results and status. "
        "Only route the tasks based on the router if there is anything to route or task is not complete. "
        "When finished, respond with FINISH." 
    ) + llama3_end_template

    return SYSTEM_PROMPT


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def routing_prompt(options, members):
    """
    This function generates a prompt for the supervisor agent to decide who should act next based on the conversation context.
    It uses the system-level prompt and follows up with the worker assignment task.
    """
    system_prompt = get_system_prompt()

    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt),
         MessagesPlaceholder(variable_name="messages"),
         (
             "system",  "Given the conversation above, who should act next? Or is the task complete and should we FINISH?  Select one of: {options}",
         ),]).partial(options=str(options), members=", ".join(members))

    return prompt


def get_search_agent_prompt():
    """
    This function generates the search agent's prompt to search for jobs based on the user's request.
    The search agent retries up to three times if no results are found.
    """
    SEARCH_AGENT = llama3_begin_template + (
        "You are a Searcher Agent. "
        "Search for job listings based on user-specified parameters, DISPLAY job title, company URL, location, and a summary. "
        "If unsuccessful, retry with alternative keywords up to three times and provide the results"
    ) + llama3_end_template

    return SEARCH_AGENT


def get_analyzer_agent_prompt():
    """
    This function generates the prompt for the analyzer agent. It analyzes the content of the user-uploaded CV
    and matches it with job listings to recommend the best job fit.
    """
    ANALYZER_AGENT = llama3_begin_template + (
        "You are an Analyzer Agent. "
        "Analyze the content of the user-uploaded CV and matching job listings to recommend the best job fit, "
        "detailing the reasons behind the choice."
    ) + llama3_end_template

    return ANALYZER_AGENT


def get_generator_agent_prompt():
    """
    This function generates the prompt for the generator agent. It creates a personalized cover letter based
    on the user-uploaded CV and matching job listings.
    """
    GENERATOR_AGENT = llama3_begin_template + (
        "You are a Generator Agent. "
        "Generate a personalized cover letter based on an uploaded CV and provide the text output."
    ) + llama3_end_template

    return GENERATOR_AGENT
