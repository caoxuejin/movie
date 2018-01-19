# coding:utf8

from datetime import datetime
from app import db


# 会员
class User(db.Model):
    __tableName__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    createTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    userLogs = db.relationship("UserLog", backref="user")  # 会员日志外键关系关联
    comments = db.relationship("Comment", backref="user")  # 评论外键关系关联
    movieCols = db.relationship("MovieCol", backref="user")  # 电影收藏外键关系关联

    def __repr__(self):
        return "<User %r>" % self.name


# 会员登录日志
class UserLog(db.Model):
    __tableName__ = "userLog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属会员
    ip = db.Column(db.String(100))  # 登录IP
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return "UserLog %r" % self.id


# 标签
class Tag(db.Model):
    __tableName__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    movies = db.relationship("Movie", backref="tag")  # 电影外键关联关系

    def __repr__(self):
        return "Tag %r" % self.name


# 电影
class Movie(db.Model):
    __tableName__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 地址
    info = db.Column(db.Text)  # 简介
    log = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    playNum = db.Column(db.BigInteger)  # 播放量
    commentNum = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))  # 所属标签
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 播放时间
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    comments = db.relationship("Comment", backref="movie")  # 评论外键关系关联
    movieCols = db.relationship("MovieCol", backref="movie")  # 电影收藏外键关系关联

    def __repr__(self):
        return "Movie %r" % self.title


# 上映预告
class Preview(db.Model):
    __tableName__ = "preview"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    logo = db.Column(db.String(255), unique=True)  # 封面
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Preview %r>" % self.title


# 评论
class Comment(db.Model):
    __tableName__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    cotent = db.Column(db.Text)  # 内容
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Comment %r>" % self.id


# 电影收藏
class MovieCol(db.Model):
    __tableName__ = "movieCol"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<MovieCol %r>" % self.id


# 权限
class Auth(db.Model):
    __tableName__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 地址
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tableName__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  # 角色列表
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    admins = db.relationship("Admin", backref="role")  # 管理员外键关系关联

    def __repr__(self):
        return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
    __tableName__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 管理员帐号
    pwd = db.Column(db.String(100))  # 管理员密码
    is_super = db.Column(db.SmallInteger)  # 是否为超级管理员，0为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))  # 所属角色
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    adminLogs = db.relationship("AdminLog", backref="admin")  # 管理员登录日志外键关系关联
    opLogs = db.relationship("OpLog", backref="admin")  # 操作日志外键关系关联

    def __repr__(self):
        return "Admin %r" % self.id

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 管理员登录日志
class AdminLog(db.Model):
    __tableName__ = "adminLog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录IP
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return "AdminLog %r" % self.id


# 操作日志
class OpLog(db.Model):
    __tableName__ = "opLog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录IP
    reason = db.Column(db.String(600))  # 操作原因
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间

    def __repr__(self):
        return "<OpLog %r>" % self.id

# if __name__ == "__main__":
#     # db.create_all()
#     """
#     role = Role(
#         name = "超级管理员",
#         auths =""
#     )
#     db.session.add(role)
#     db.session.commit()
#     """
#     from werkzeug.security import generate_password_hash
#
#     admin = Admin(
#         name = "imooc",
#         pwd = generate_password_hash("caoxuejin"),
#         is_super = 0,
#         role_id = 1
#     )
#     db.session.add(admin)
#     db.session.commit()
