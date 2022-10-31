import json
from uuid import UUID
from datetime import date
from datetime import datetime
from typing import Optional, List


from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

from fastapi import FastAPI
from fastapi import status
from fastapi import Body

app = FastAPI()


# Models
class Base_User(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class User_Pass(Base_User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=25
    )


class User(Base_User):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birthdate: Optional[date] = Field(default=None)


class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=25
    )


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["tweets"]
)
def home():
    with open("./tweets.json", "r", encoding="utf-8") as f:
        tweets = json.loads(f.read())
        return tweets


@app.post(
    path="/tweets/created",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["tweets"]
)
def post_a_tweet(tweet: Tweet = Body(...)):
    with open("./tweets.json", "r+", encoding="utf-8") as f:
        result = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birthdate"] = str(tweet_dict["by"]["birthdate"])
        result.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(result))
        return tweet


@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="show a tweet",
    tags=["tweets"]
)
def show_a_tweet():
    pass


@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="delete an tweet",
    tags=["tweets"]
)
def delete_a_tweet():
    pass


@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="update a tweet",
    tags=["tweets"]
)
def update_a_tweet():
    pass


@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register an User",
    tags=["users"]
)
def signup(user: UserRegister = Body(...)):
    """
    Signup.

    This path operation register a user in the app

    Parameters:
        - Request body parameter:
            - user: UserRegister
    Returns a json with the basic user information:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        -birth_date: datetime

    """
    with open("./users.json", "r+", encoding="utf-8") as f:
        result = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birthdate"] = str(user_dict["birthdate"])
        result.append(user_dict)
        f.seek(0)
        f.write(json.dumps(result))
        return user


@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login an User",
    tags=["users"]
)
def login():
    pass


@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_201_CREATED,
    summary="Show all User",
    tags=["users"]
)
def show_all_users():
    """
    This path operation shows all users in the app

    parameters:
    -

    returns a json list with all users in the app, with following keys:
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        -birth_date: datetime
    """
    with open("./users.json", "r", encoding="utf-8") as f:
        users = json.loads(f.read())
        return users


@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show an User",
    tags=["users"]
)
def show_a_user():
    pass


@app.delete(
    path="/user/{user_id}/delete}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete an User",
    tags=["users"]
)
def delete_a_user():
    pass


@app.put(
    path="/user/{user_id}/update}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update an User",
    tags=["users"]
)
def update_a_user():
    pass
