{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "201350e0-3752-42fb-81b7-a883e098b09b",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [23]\u001b[0m, in \u001b[0;36m<cell line: 21>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      6\u001b[0m qa_pairs \u001b[38;5;241m=\u001b[39m [\n\u001b[0;32m      7\u001b[0m     [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m(.*)name(.*)\u001b[39m\u001b[38;5;124m'\u001b[39m,[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhello this is swiggy\u001b[39m\u001b[38;5;124m'\u001b[39m]],\n\u001b[0;32m      8\u001b[0m     [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m(.*)food(.*)\u001b[39m\u001b[38;5;124m'\u001b[39m,[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mwhich type of food do you prefer now north indian,south indian,chinese,italian\u001b[39m\u001b[38;5;124m'\u001b[39m]],\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m     17\u001b[0m     \n\u001b[0;32m     18\u001b[0m ]\n\u001b[0;32m     20\u001b[0m cb \u001b[38;5;241m=\u001b[39m Chat(qa_pairs)\n\u001b[1;32m---> 21\u001b[0m \u001b[43mcb\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mconverse\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\nltk\\chat\\util.py:118\u001b[0m, in \u001b[0;36mChat.converse\u001b[1;34m(self, quit)\u001b[0m\n\u001b[0;32m    116\u001b[0m user_input \u001b[38;5;241m=\u001b[39m quit\n\u001b[0;32m    117\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 118\u001b[0m     user_input \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43minput\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43m>\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m    119\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mEOFError\u001b[39;00m:\n\u001b[0;32m    120\u001b[0m     \u001b[38;5;28mprint\u001b[39m(user_input)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py:1075\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1071\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_allow_stdin:\n\u001b[0;32m   1072\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(\n\u001b[0;32m   1073\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1074\u001b[0m     )\n\u001b[1;32m-> 1075\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_input_request\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   1076\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mprompt\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1077\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_parent_ident\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1078\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_parent\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mshell\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1079\u001b[0m \u001b[43m    \u001b[49m\u001b[43mpassword\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\n\u001b[0;32m   1080\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py:1120\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1117\u001b[0m             \u001b[38;5;28;01mbreak\u001b[39;00m\n\u001b[0;32m   1118\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[0;32m   1119\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[1;32m-> 1120\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28mNone\u001b[39m\n\u001b[0;32m   1121\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1122\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "#importing libraries\n",
    "from flask import Flask, render_template, request\n",
    "import nltk\n",
    "from nltk.chat.util import Chat\n",
    "\n",
    "qa_pairs = [\n",
    "    ['(.*)name(.*)',['hello this is swiggy']],\n",
    "    ['(.*)food(.*)',['which type of food do you prefer now north indian,south indian,chinese,italian']],\n",
    "    ['(.*)(hi|Hello)(.*)',['hello how can i help you']],\n",
    "    ['(.*)(north indian|south indian|chinese|italian)(.*)',['Here here is list item']],\n",
    "    ['(.*)(hungry|hurry|fast|delivery late)(.*)',['Your order is on the way']],\n",
    "    ['(.*)menu(.*)',['select a choice north indian,south indian,chinese,italian']],\n",
    "    ['what should i prefer',['(you can try north india|you can try south indian|you can try chinese|you can try italian']],\n",
    "    ['(.*)offer(.*)',['here is todays offer']],\n",
    "    ['(.*)coupans(.*)',['you can apply these']],\n",
    "    ['(.*)',['sorry i dont know this']]\n",
    "    \n",
    "]\n",
    "\n",
    "cb = Chat(qa_pairs)\n",
    "\n",
    "@app.route('/',methods= ['POST'])\n",
    "def chatbot_response():\n",
    "    response = ''\n",
    "    if request.method == 'POST':\n",
    "        msg = request.form[message]\n",
    "        response = cb.respond(msg)\n",
    "    return render_template('index.html',response1 = response)\n",
    "\n",
    "if__name__=='__main__':\n",
    "    app.run(debug=True)\n",
    "    \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "3106d2ba-39da-4747-b963-c4c25faa758c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47d2b87b-da28-40c1-ba54-cf1829720ded",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
