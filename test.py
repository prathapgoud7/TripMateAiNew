from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import database_connection, GROQ_API_KEY, llm, TravelState, flight_agent, hotel_agent, itinerary_agent,run_travel_agent
# res=tavily_search("Best hotels in Europe")
user_input=input("Enter your travel query: ")
res=run_travel_agent(user_input=user_input,thread_id="user_id")
print(res)
