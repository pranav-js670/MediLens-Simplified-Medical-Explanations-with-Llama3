from django.shortcuts import render
from django.shortcuts import render, redirect

from .models import Transcripts



from langchain.document_loaders import UnstructuredFileLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from transformers import pipeline

# Define your Groq API key
GROQ_API_KEY = "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"
llm = ChatGroq(groq_api_key=GROQ_API_KEY, model="Llama3-8b-8192")
# Function to generate responses
def answer_query(question, context):
    # Create text chunks and generate embeddings
    text_splitter = CharacterTextSplitter(separator='\n', chunk_size=2000, chunk_overlap=200)
    documents = text_splitter.create_documents([context])

    embeddings = HuggingFaceEmbeddings()

    # Create a FAISS index
    faiss_index = FAISS.from_documents(documents, embeddings)

    # Define the prompt template with simplified explanations
    prompt_template = """
    You are a helpful assistant who explains complex medical terms in extremely simplified language suitable for someone with no medical background. Below is the medical information for a patient. For each term, provide a clear and simple explanation.

    If the question asks for a specific detail, such as the patient's name or age, provide only that detail without additional information.

    Examples:
    1. Medical text:
       Name: Mr. Johnson
       Symptoms: Fatigue, dizziness, shortness of breath
       Diagnosis: Faulty heart valve

       Question: What is a heart valve?
       Helpful Answer: A heart valve is a door-like structure in the heart that controls the flow of blood. If it becomes faulty, it may cause problems with blood flow.

    2. Medical text:
       Name: Mr. Johnson
       Symptoms: Fatigue, dizziness, shortness of breath
       Diagnosis: Faulty heart valve

       Question: What is valve replacement surgery?
       Helpful Answer: Valve replacement surgery is a procedure to replace a damaged or faulty heart valve with an artificial or biological valve.

    Please provide similar explanations for the following terms based on the context:
    {context}

    Question: {question}
    Helpful Answer:
    """

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Set up RAG with the Model
    knowledge_base = faiss_index

    # Set up RetrievalQA with the correct prompt template
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=knowledge_base.as_retriever(),
        chain_type_kwargs={"prompt": PROMPT}
    )

    # Get response from the model
    response = qa_chain({"context": context, "question": question, "query":question})
    return response["result"]


from Bio_Epidemiology_NER.bio_recognizer import ner_prediction


def doctor(request):
    if request.method == "POST":
        medical_text = request.POST.get('text')
        if not medical_text:  # Check if medical_text is empty
            return render(request, 'doctor.html')  # Render the doctor.html again

        transript_section = Transcripts(text=medical_text)
        transript_section.save()
        if request.POST.get('submit_button') == 'submit1':
            return redirect('main:patient', transcript_id=transript_section.id)
        elif request.POST.get('submit_button') == 'submit2':
            return redirect('main:patient_cards', transcript_id=transript_section.id)

    return render(request, 'doctor.html')


#medical_text = "Mr. Johnson, I understand that you've been experiencing symptoms such as fatigue, dizziness, and shortness of breath lately. After reviewing your tests, it appears that you have a faulty heart valve that requires replacement. Don't worry; valve replacement surgery is a common and highly effective procedure. Before the surgery, it's important to follow some precautions. Avoid any strenuous activities and stick to a heart-healthy diet to prepare your body. After the surgery, you'll need to take it easy for a while and gradually increase your activity level as advised by your medical team. Remember to follow all post-operative instructions diligently to ensure a smooth recovery process. If you have any concerns or questions, feel free to discuss them with us. We're here to support you every step of the way."

from django.shortcuts import render
from django.http import JsonResponse
from .models import Transcripts

def patient(request, transcript_id):
    transcript = Transcripts.objects.get(id=transcript_id)
    medical_text = transcript.text
    question2 = ("""Convey the entire prescription understandable to an extreme illeterate person. Directly start saying the content.
                 Do: 'Mr. X you are ...'
                 Dont: 'Here's a simplified explanation of the prescription: "So, Mr. Johnson'
                 Give it very detailed point to point and understandable""")
    response2 = answer_query(question2, medical_text)
    return render(request, 'patient.html', {'response': response2, 'query_answer': 'Ask questions'})

from django.http import JsonResponse

def get_query_answer(request):
    print("OK")
    if request.method == "POST":
        question = request.POST.get('question')
        content = request.POST.get('response')
        print("Q: ",question, "A: ", content)
        print("NOT OK")
        # Process the question and get the answer
        query_answer = answer_query(question, content )
        return JsonResponse({'query_answer': query_answer})
    else:
        return JsonResponse({'error': 'Invalid request'})



def patient_card(request, transcript_id):
    transcript = Transcripts.objects.get(id=transcript_id)
    medical_text = transcript.text

    segmentations = ner_prediction(corpus=medical_text, compute='cpu')  # pass compute='gpu' if using gpu
    mapper = {}
    for index, row in segmentations.iterrows():
        key = row['entity_group']
        value = row['value']
        score = row['score']

        if key not in mapper:
            mapper[key] = []
        mapper[key].append(value)

    return render(request, 'patient_cards.html', {'mapper': mapper})



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#
# @csrf_exempt
# def send_text(request):
#     if request.method == "POST":
#         question = request.POST.get('questionInput')
#         print(question)
#         # Perform processing on the received text (e.g., answer_query(question, medical_text))
#         response = answer_query(question, medical_text)
#         response_data = {'response': response}
#         return JsonResponse(response_data)
#     else:
#         return JsonResponse({'error': 'Invalid request method.'})



