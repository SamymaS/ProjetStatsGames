// // frontend/src/utils/api.js

// import axios from 'axios';

// const api = axios.create({
//   baseURL: 'http://127.0.0.1:8000/api/', // Mettez l'URL de votre API Django
// });

// export default api;

import axios from 'axios';

const baseURL = 'http://localhost:8000'; // URL of your Django backend

const api = axios.create({
  baseURL: baseURL,
});

const login = async (username, password) => {
  return await api.post('/api/login/', { username, password });
};

const register = async (username, password) => {
  return await api.post('/api/register/', { username, password });
};

export default {
  login,
  register,
};
