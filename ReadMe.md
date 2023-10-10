# AcademyConnect


## Запуск проекта с использованием Docker

1. **Установите Docker:**
   - [Инструкции по установке Docker](https://docs.docker.com/get-docker/)

2. **Клонируйте репозиторий проекта:**

   ```bash
   git clone https://github.com/ваш-пользователь/https://github.com/Memorizu/AcademyConnect.git
   cd AcademyConnect
   
3. **Создайте файл .env в корневой папке проекта и укажите в нем необходимые переменные окружения:**
    
   ```
    POSTGRES_PASSWORD=
    ADMIN_PASSWORD=
    USER_PASSWORD=
    
    SECRET_KEY=
    
    STRIPE_KEY=
    PUBLISHEBLE_KEY=

4. **Соберите и запустите Docker контейнеры:**
    
    ```
        docker-compose up --build
**Это соберет и запустит контейнеры, необходимые для работы проекта.**