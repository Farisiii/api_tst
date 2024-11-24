from werkzeug.security import generate_password_hash
from typing import Dict, List

# Database simulation
users_db: Dict[str, dict] = {
    "example@email.com": {
        "password": generate_password_hash("password123"),
        "role": "user"
    },
    "admin@email.com": {
        "password": generate_password_hash("admin123"),
        "role": "admin"
    }
}

services_db: List[dict] = [
  {
    "id": 1,
    "type": "Massage",
    "provider": {
      "id": 103,
      "name": "Provider 3",
      "image": "provider_3.jpg",
      "rating": 4.4,
      "reviews": 90
    },
    "rate": 40,
    "availability": [
      {
        "date": "2023-05-01",
        "slots": [
          {
            "start": "07:00",
            "end": "07:30"
          },
          {
            "start": "08:30",
            "end": "09:00"
          },
          {
            "start": "10:00",
            "end": "10:30"
          },
          {
            "start": "11:30",
            "end": "12:00"
          },
          {
            "start": "13:00",
            "end": "13:30"
          },
          {
            "start": "14:30",
            "end": "15:00"
          },
          {
            "start": "16:00",
            "end": "16:30"
          },
          {
            "start": "17:30",
            "end": "18:00"
          },
          {
            "start": "19:00",
            "end": "19:30"
          }
        ]
      },
      {
        "date": "2023-05-02",
        "slots": [
          {
            "start": "07:00",
            "end": "07:30"
          },
          {
            "start": "08:30",
            "end": "09:00"
          },
          {
            "start": "10:00",
            "end": "10:30"
          },
          {
            "start": "11:30",
            "end": "12:00"
          },
          {
            "start": "13:00",
            "end": "13:30"
          },
          {
            "start": "14:30",
            "end": "15:00"
          },
          {
            "start": "16:00",
            "end": "16:30"
          },
          {
            "start": "17:30",
            "end": "18:00"
          },
          {
            "start": "19:00",
            "end": "19:30"
          }
        ]
      },
      {
        "date": "2023-05-03",
        "slots": [
          {
            "start": "07:00",
            "end": "07:30"
          },
          {
            "start": "08:30",
            "end": "09:00"
          },
          {
            "start": "10:00",
            "end": "10:30"
          },
          {
            "start": "11:30",
            "end": "12:00"
          },
          {
            "start": "13:00",
            "end": "13:30"
          },
          {
            "start": "14:30",
            "end": "15:00"
          },
          {
            "start": "16:00",
            "end": "16:30"
          },
          {
            "start": "17:30",
            "end": "18:00"
          },
          {
            "start": "19:00",
            "end": "19:30"
          }
        ]
      }
    ]
  },
  {
    "id": 2,
    "type": "Housekeeping",
    "provider": {
      "id": 104,
      "name": "Provider 4",
      "image": "provider_4.jpg",
      "rating": 4.6,
      "reviews": 110
    },
    "rate": 50,
    "availability": [
      {
        "date": "2023-05-01",
        "slots": [
          {
            "start": "07:00",
            "end": "07:30"
          },
          {
            "start": "08:30",
            "end": "09:00"
          },
          {
            "start": "10:00",
            "end": "10:30"
          },
          {
            "start": "11:30",
            "end": "12:00"
          },
          {
            "start": "13:00",
            "end": "13:30"
          },
          {
            "start": "14:30",
            "end": "15:00"
          },
          {
            "start": "16:00",
            "end": "16:30"
          },
          {
            "start": "17:30",
            "end": "18:00"
          },
          {
            "start": "19:00",
            "end": "19:30"
          }
        ]
      },
      {
        "date": "2023-05-02",
        "slots": [
          {
            "start": "07:00",
            "end": "07:30"
          },
          {
            "start": "08:30",
            "end": "09:00"
          },
          {
            "start": "10:00",
            "end": "10:30"
          },
          {
            "start": "11:30",
            "end": "12:00"
          },
          {
            "start": "13:00",
            "end": "13:30"
          },
          {
            "start": "14:30",
            "end": "15:00"
          },
          {
            "start": "16:00",
            "end": "16:30"
          },
          {
            "start": "17:30",
            "end": "18:00"
          },
          {
            "start": "19:00",
            "end": "19:30"
          }
        ]
      },
      {
        "date": "2023-05-03",
        "slots": [
          {
            "start": "07:00",
            "end": "07:30"
          },
          {
            "start": "08:30",
            "end": "09:00"
          },
          {
            "start": "10:00",
            "end": "10:30"
          },
          {
            "start": "11:30",
            "end": "12:00"
          },
          {
            "start": "13:00",
            "end": "13:30"
          },
          {
            "start": "14:30",
            "end": "15:00"
          },
          {
            "start": "16:00",
            "end": "16:30"
          },
          {
            "start": "17:30",
            "end": "18:00"
          },
          {
            "start": "19:00",
            "end": "19:30"
          }
        ]
      }
    ]
  },
  {
    "id": 3,
    "type": "Gardening",
    "provider": {
      "id": 104,
      "name": "Provider 4",
      "image": "provider_4.jpg",
      "rating": 4.6,
      "reviews": 110
    },
    "rate": 60,
    "availability": [
      {
        "date": "2023-05-01",
        "slots": [
          {
            "start": "07:00",
            "end": "07:30"
          },
          {
            "start": "08:30",
            "end": "09:00"
          },
          {
            "start": "10:00",
            "end": "10:30"
          },
          {
            "start": "11:30",
            "end": "12:00"
          },
          {
            "start": "13:00",
            "end": "13:30"
          },
          {
            "start": "14:30",
            "end": "15:00"
          },
          {
            "start": "16:00",
            "end": "16:30"
          },
          {
            "start": "17:30",
            "end": "18:00"
          },
          {
            "start": "19:00",
            "end": "19:30"
          }
        ]
      },
      {
        "date": "2023-05-02",
        "slots": [
          {
            "start": "07:00",
            "end": "07:30"
          },
          {
            "start": "08:30",
            "end": "09:00"
          },
          {
            "start": "10:00",
            "end": "10:30"
          },
          {
            "start": "11:30",
            "end": "12:00"
          },
          {
            "start": "13:00",
            "end": "13:30"
          },
          {
            "start": "14:30",
            "end": "15:00"
          },
          {
            "start": "16:00",
            "end": "16:30"
          },
          {
            "start": "17:30",
            "end": "18:00"
          },
          {
            "start": "19:00",
            "end": "19:30"
          }
        ]
      },
      {
        "date": "2023-05-03",
        "slots": [
          {
            "start": "07:00",
            "end": "07:30"
          },
          {
            "start": "08:30",
            "end": "09:00"
          },
          {
            "start": "10:00",
            "end": "10:30"
          },
          {
            "start": "11:30",
            "end": "12:00"
          },
          {
            "start": "13:00",
            "end": "13:30"
          },
          {
            "start": "14:30",
            "end": "15:00"
          },
          {
            "start": "16:00",
            "end": "16:30"
          },
          {
            "start": "17:30",
            "end": "18:00"
          },
          {
            "start": "19:00",
            "end": "19:30"
          }
        ]
      }
    ]
  }
]