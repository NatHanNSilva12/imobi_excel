import os

class Config:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'J9IJBBH575Vs3EO5vDRPaL7nV6E80EGmUaAX+TW98XRmAfl7usDiYy3alx1WizhpU9gWQ6gDlDI8PbiilPtRHQ==')
    SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://uxqxjdfvtlrkjaepjdwp.supabase.co')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV4cXhqZGZ2dGxya2phZXBqZHdwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg5MTE2NDAsImV4cCI6MjA0NDQ4NzY0MH0.BVqcKB3UZ_KW8GXJaQVeLqfXsOuVy3chIFTXTgKztLE')
    
    EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT = 587
    EMAIL_USER = os.environ.get('EMAIL_USER', 'seuemail@dominio.com')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', 'sua_senha')

config = Config()
