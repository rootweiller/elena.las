
Endpoints para la creacion de perfiles y asinaturas

{
    "registration": "http://127.0.0.1:8000/profile/registration/",
    "subject/create": "http://127.0.0.1:8000/profile/subject/create/"
}


Metodos soportados
- POST
- GET


Para registro de Perfil

Payload:
{
	"first_name": "Juan",
	"last_name": "Vargas",
	"email": "juan@juan7.com",
	"username": "unnick9",
	"user": 1,
	"phone": "5712345677",
	"subject": 2
}

