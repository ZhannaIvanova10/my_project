from setuptools import setup, find_packages

setup(
    name="my_project",  # Название вашего проекта
    version="0.1.0",    # Версия проекта
    packages=find_packages(where="src"),  # Ищем пакеты в папке src
    package_dir={"": "src"},  # Указываем, что пакеты находятся в src
    python_requires=">=3.10",  # Минимальная версия Python
)