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

## 📑 Example Usage


### 1. GET Request

Retrieve data from an external API.

**Request:**
```bash
curl -X GET "http://localhost:5000/?url=https://jsonplaceholder.typicode.com/posts"
```

**Response:**
```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit..."
  },
  ...
]
```

<details>
<summary>Click to expand</summary>


### 2. POST Request

Send data to an external API.

**Request:**
```bash
curl -X POST "http://localhost:5000/?url=https://jsonplaceholder.typicode.com/posts" \
-H "Content-Type: application/json" \
-d '{"title": "foo", "body": "bar", "userId": 1}'
```

**Response:**
```json
{
  "id": 101,
  "title": "foo",
  "body": "bar",
  "userId": 1
}
```

### 3. PUT Request

Update existing data at an external API.

**Request:**
```bash
curl -X PUT "http://localhost:5000/?url=https://jsonplaceholder.typicode.com/posts/1" \
-H "Content-Type: application/json" \
-d '{"id": 1, "title": "updated title", "body": "updated body", "userId": 1}'
```

**Response:**
```json
{
  "id": 1,
  "title": "updated title",
  "body": "updated body",
  "userId": 1
}
```

### 4. DELETE Request

Delete data at an external API.

**Request:**
```bash
curl -X DELETE "http://localhost:5000/?url=https://jsonplaceholder.typicode.com/posts/1"
```

**Response:**
```json
{
  "message": "Post deleted successfully"
}
```

### 5. PATCH Request

Partially update data at an external API.

**Request:**
```bash
curl -X PATCH "http://localhost:5000/?url=https://jsonplaceholder.typicode.com/posts/1" \
-H "Content-Type: application/json" \
-d '{"title": "patched title"}'
```

**Response:**
```json
{
  "id": 1,
  "title": "patched title",
  "body": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "userId": 1
}
```

### 6. OPTIONS Request

Check which HTTP methods are supported by the external API.

**Request:**
```bash
curl -X OPTIONS "http://localhost:5000/?url=https://jsonplaceholder.typicode.com/posts"
```

**Response:**
```http
HTTP/1.1 200 OK
Allow: GET, POST, PUT, DELETE, PATCH, OPTIONS
```

</details>

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
