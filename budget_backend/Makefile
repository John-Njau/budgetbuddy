install:
	@echo "Installing $(NAME) to $(DESTDIR)$(PREFIX)/bin"
	pip install -r requirements.txt

serve:
	@echo "Serving on http://localhost:8000"
	python manage.py runserver

migration:
	@echo "Creating migration"
	python manage.py makemigrations
	@echo "Migrating"
	python manage.py migrate

test:
	@echo "Running tests"
	python manage.py test

clean:
	@echo "Cleaning up"
	rm -rf .pytest_cache

superuser:
	@echo "Creating superuser"
	python manage.py createsuperuser

