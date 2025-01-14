from flask import Blueprint, render_template, request, redirect, flash, session
from ..extentions import db
from ..config import PASSWORD, LOGINN

LogOut = Blueprint('LogOut', __name__)

@LogOut.route("/LogOut")
def LOGOUT():
    session.pop('user', None)  # Удаляем пользователя из сессии
    session.pop('role', None)  # Удаляем роль
    return redirect('/')
    
