"""Renders and Flasks the website"""
from flask import Flask, request, make_response
from flask import render_template
import requests
from luxinfo import get_info
from luxdetails import get_object_info

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """homepage url and methodologies"""
    label = request.args.get('l', '')
    classifier = request.args.get('c', '')
    agent = request.args.get('a', '')
    date = request.args.get('d', '')

    if not any([label, classifier, agent, date]):
        label = request.cookies.get('prev_search_label', '')
        classifier = request.cookies.get('prev_search_classifier', '')
        agent = request.cookies.get('prev_search_agent', '')
        date = request.cookies.get('prev_search_date', '')

    row = None
    if any([label, classifier, agent, date]):
        row = get_info(date, agent, classifier, label)
        if not row:
            error_message = "No results found."
        else:
            error_message = None
    else:
        error_message = request.args.get('error_message', None)

    html = render_template('index.html',
        prev_search_label=label,
        prev_search_classifier=classifier,
        prev_search_agent=agent,
        prev_search_date=date,
        row=row, error_message=error_message)


    response = make_response(html)
    if row:

        response.set_cookie('prev_search_label', label)
        response.set_cookie('prev_search_classifier', classifier)
        response.set_cookie('prev_search_agent', agent)
        response.set_cookie('prev_search_date', date)
    return response

@app.route('/search', methods=['GET'])
def search():
    """for url ending with /search?..."""
    label = request.args.get('l')
    classifier = request.args.get('c')
    agent = request.args.get('a')
    date = request.args.get('d')

    if not any([label, classifier, agent, date]):
        error_message = "Please enter at least one search parameter."
        return render_template('index.html', error_message=error_message)

    if (label is None) or (label.strip() == ''):
        label = ''
    if (classifier is None) or (classifier.strip() == ''):
        classifier = ''
    if (agent is None) or (agent.strip() == ''):
        agent = ''
    if (date is None) or (date.strip() == ''):
        date = ''

    row = get_info(date, agent, classifier, label)

    if not row:
        no_results_message = "The provided parameters didn't match any results in our database."
        return render_template('index.html', no_results_message=no_results_message)

    html = render_template('index.html', row=row)
    response = make_response(html)

    response.set_cookie('prev_search_label', label)
    response.set_cookie('prev_search_classifier', classifier)
    response.set_cookie('prev_search_agent', agent)
    response.set_cookie('prev_search_date', date)

    return response

@app.route('/object')
def object_error():
    """Gives error message for incorrect object url"""
    # Return an error page with a message and a 404 status code
    return render_template('error.html', message="Error: missing object id."), 404

@app.route('/object/<int:object_id>')
def object_details(object_id):
    """Gives object's details, like our luxdetails"""
    summary, label, produced_by, classified_as, information = get_object_info(object_id)

    # Determine whether the object has an image (modify this logic accordingly)
    image_url_test = f"https://media.collections.yale.edu/thumbnail/yuag/obj/{object_id}"
    image_response = requests.get(image_url_test, timeout=20)

    # Construct the image URL based on whether the object has an image
    if image_response.status_code == 200:
        image_url = f"https://media.collections.yale.edu/thumbnail/yuag/obj/{object_id}"
    else:
        image_url = None  # No image available


    html = render_template('object_details.html',
        object_id = object_id,
        summary=summary, label=label,
        produced_by=produced_by,
        classified_as=classified_as,
        information=information,
        image_url=image_url)

    response = make_response(html)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
