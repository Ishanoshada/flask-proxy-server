# 🌐 Flask Proxy Server

![GitHub stars](https://img.shields.io/github/stars/ishanoshada/flask-proxy-server?style=social) ![GitHub forks](https://img.shields.io/github/forks/ishanoshada/flask-proxy-server?style=social) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

Welcome to **Flask Proxy Server**! This project is a powerful and secure proxy server built using Flask. It provides enhanced input validation, domain whitelisting/blacklisting, header management, and IP-based access control, all while being simple to set up and use.

---

## ✨ Features

- **URL Sanitization & Validation**: Ensures only clean and safe URLs are processed.
- **Domain Control**: Implement domain whitelisting and blacklisting to control access.
- **Header Management**: Automatically filters out potentially problematic headers.
- **IP Access Control**: Restrict server access based on IP addresses.
- **Request Caching**: Cache successful GET requests for faster response times.
- **Detailed Logging**: Keep track of all requests with comprehensive logging.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your machine.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ishanoshada/flask-proxy-server.git
   cd flask-proxy-server
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**:
   ```bash
   python api/app.py
   ```

4. **Make your first request**:
   Open your browser or use a tool like Postman to test the proxy:
   ```
   http://localhost:5000/?url=https://jsonplaceholder.typicode.com/posts
   ```

---

## 🔧 Configuration

Customize the server's behavior by modifying the following variables in `api/app.py`:

- **Allowed Domains**:
  - Update `WHITELISTED_DOMAINS` and `BLACKLISTED_DOMAINS` to control which domains can be accessed.

- **IP Restrictions**:
  - Modify `ALLOWED_IPS` to specify which IP addresses can access the server.




## 🌍 Deployment with Vercel

To deploy this Flask application on Vercel, follow these steps:

1. **Login to Vercel**:
   If you don’t have a Vercel account, create one and log in via the CLI.
   ```bash
   npm i -g vercel
   vercel login
   ```

2. **Deploy the Project**:
   Navigate to your project directory and deploy:
   ```bash
   vercel
   ```
   Follow the prompts to set up your project and select your preferences.

3. **Environment Variables**:
   If your application requires any environment variables (like secrets), set them in your Vercel dashboard under the Environment Variables section.


---

## 🧪 Testing

Ensure your proxy works correctly by writing and running tests. Consider using tools like `pytest` to automate your testing process.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📣 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request or open an issue. Let's make this project even better together!

---

## 🙌 Acknowledgements

- Thanks to the Flask community for creating such a powerful framework!

---

## 🌟 Get in Touch

If you have any questions or feedback, feel free to reach out:

- **GitHub**: [ishanoshada](https://github.com/ishanoshada)


Happy coding! 🎉
