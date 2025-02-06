from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

basic_prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
    [
        ("system", "You are the assistant of general knowledge."),
        ("system", "Answer in the same language as the one of question."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)
