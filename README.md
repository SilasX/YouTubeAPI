#### Installation

Clone the repo, and set up a virtual environment from the root directory:

    virtualenv venv
    . ./venv/bin/activate

Install dependencies

    pip install -r requirements.txt

#### Usage

As written so far, it pulls the name, url, category, and thumbnail for the top 25 most viewed YouTube videos of the past week.

To do that, instantiate a `Request` object and call `get_most_viewed_all` on it.

    r = Request()
    r.get_most_viewed_all()

The resulting `.result` property is a `Result` object, on which you can call certain methods.  `.key_elements()` returns the results as a list of dictionaries.

    r1.result.key_elements()

To render as a table in html, just call `.render_html()` on the result object:

    r1.result.render_html()

#### Tests

Run the tests with `nosetests` which installs with the requirements.
