import wolframalpha

#From https://www.geeksforgeeks.org/python-create-a-simple-assistant-using-wolfram-alpha-api/
def DAVIDwolframalpha(text):
    app_id = "TLPAPR-VXEYQKW7AL"
    client = wolframalpha.Client(app_id)
    res = client.query(text)
    answer = next(res.results).text
    return answer

def testDAVIDwolframalpha():
    print('Testing DAVIDwolframalpha()...', end='')
    sample1 = "what is the capital of France"
    assert(DAVIDwolframalpha(sample1) == "Paris, Ile-de-France, France")
    sample2 = "What is the population of North Korea?"
    assert(DAVIDwolframalpha(sample2) == "25.5 million people (world rank: 52nd) (2017 estimate)")
    sample3 = "What is the area of a triangle"
    assert(DAVIDwolframalpha(sample3) == "1/4 sqrt((a + b - c) (a - b + c) (-a + b + c) (a + b + c))")
    sample4 = "How old is Donald Trump?"
    assert(DAVIDwolframalpha(sample4) == "73 years 9 months 20 days")
    print('Passed!')
