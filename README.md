# Flask Test Application

A simple Flask web application that demonstrates basic web development concepts and testing.

## Features

- Simple "Hello World" endpoint
- Built-in test suite
- Docker support
- CI/CD pipeline configuration

## Prerequisites

- Python 3.x
- pip (Python package manager)
- Docker (optional, for containerization)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd AutomatedProject-main
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development
```bash
python app.py
```
The application will be available at `http://localhost:8080`

### Using Docker
```bash
docker build -t flasktest-app .
docker run -p 8080:8080 flasktest-app
```

## Testing

Run the test suite using:
```bash
python -m pytest test_app.py
```

## Project Structure

- `app.py` - Main Flask application
- `test_app.py` - Test suite
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker configuration
- `.github/workflows/cicd.yaml` - CI/CD pipeline configuration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Pratyksh Gupta

## Flask App: Using GitHub Actions And Deployment On GCP!
This is a flask app whose CI/CD pipeline in available on Github Actions And Deployment has been done through Google Cloud Platform.

## Set Up Instructions:

- Clone the repository
- Install the dependencies from requirements.txt
- Activate a virtual environment
- Run the app.py file!

## Deployed Link:

You can access the deployed link here: https://flasktest-app-520982302184.us-central1.run.app/

## OutPut
Once you run the app your output should be:
<img width="1013" alt="Screenshot 2025-05-31 at 5 03 51 PM" src="https://github.com/user-attachments/assets/be429937-ed18-44f4-b582-016b68850ca0" />
