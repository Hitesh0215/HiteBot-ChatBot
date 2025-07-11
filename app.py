{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e2d70531-3cb5-4365-b1b2-edc2675fd4d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "from flask_cors import CORS\n",
    "from datetime import datetime\n",
    "\n",
    "app = Flask(__name__)\n",
    "CORS(app)\n",
    "\n",
    "def get_response(user_input, user_name=\"You\"):\n",
    "    user_input = user_input.lower().strip()\n",
    "    if \"hello\" in user_input or \"hi\" in user_input:\n",
    "        return \"Hey hey! Great to hear from you 😄\"\n",
    "    elif \"how are you\" in user_input:\n",
    "        return \"I’m doing fantastic\"\n",
    "    elif \"your name\" in user_input or \"who are you\" in user_input:\n",
    "        return \"I'm HiteBot, your helpful AI buddy coded by Hitesh \"\n",
    "    elif \"time\" in user_input or \"clock\" in user_input:\n",
    "        now = datetime.now().strftime(\"%I:%M %p\")\n",
    "        return f\"It's currently {now}. ⏰\"\n",
    "    elif \"joke\" in user_input:\n",
    "        return \"Why do Java developers wear glasses? Because they can't C#! 😂\"\n",
    "    elif \"sad\" in user_input or \"tired\" in user_input or \"bored\" in user_input:\n",
    "        return \"Sounds like you need a boost. Want a joke, a fact, or a motivational quote? 🌈\"\n",
    "    elif \"what's up\" in user_input or \"how's it going\" in user_input:\n",
    "        return \"Just chilling in cyberspace. What’s happening in your world?\"\n",
    "    elif \"bye\" in user_input or \"exit\" in user_input or \"quit\" in user_input:\n",
    "        return f\"Catch you later, {user_name}! You’ve got this. 👋\"\n",
    "    else:\n",
    "        return \"Hmm... That one flew over my antenna. Mind rephrasing it? 🤔\"\n",
    "\n",
    "@app.route('/api/chat', methods=['POST'])\n",
    "def chat():\n",
    "    data = request.get_json()\n",
    "    user_input = data.get('user_input', '')\n",
    "    response = get_response(user_input)\n",
    "    return jsonify({'response': response})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "64782b4c-afb1-4018-b86f-9256266fb516",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in c:\\users\\sharm\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (3.1.1)\n",
      "Requirement already satisfied: flask-cors in c:\\users\\sharm\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (6.0.1)\n",
      "Requirement already satisfied: blinker>=1.9.0 in c:\\users\\sharm\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (1.9.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\sharm\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (8.2.1)\n",
      "Requirement already satisfied: itsdangerous>=2.2.0 in c:\\users\\sharm\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (2.2.0)\n",
      "Requirement already satisfied: jinja2>=3.1.2 in c:\\users\\sharm\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (3.1.4)\n",
      "Requirement already satisfied: markupsafe>=2.1.1 in c:\\users\\sharm\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (2.1.5)\n",
      "Requirement already satisfied: werkzeug>=3.1.0 in c:\\users\\sharm\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from flask) (3.1.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\sharm\\appdata\\local\\programs\\python\\python312\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 24.0 -> 25.1.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "!pip install flask flask-cors\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8a22090-493a-40cb-9899-5a52e1b1af12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "app.run(debug=True, use_reloader=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0057bf6f-a106-4058-afc1-ec1461c11f51",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
