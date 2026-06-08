class Config:

    SECRET_KEY = "railway_dpms_secret"

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres.xvcvyitkrckakjhobsuv:Qwerty%40Asdfgh%40123@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False