from services.db.model import Url
from services.db.db_client import session


class UrlService:
    def __init__(self, client_session = None):
        self.current_session = client_session if client_session else session
    
    def get_original_url(self, short_code) -> str | None:
        url = self.current_session.query(Url).filter_by(short_url=short_code).first()
        return url.long_url

    def get_short_code(self, original_url) -> str | None:
        url = self.current_session.query(Url).filter_by(long_url=original_url).first()
        return url
    
    def add_url(self, original_url, short_code) -> None:
        url = Url(long_url=original_url, short_url=short_code)
        try:
            self.current_session.add(url)
            self.current_session.commit()
            self.current_session.refresh(url)
        except Exception as e:
            self.current_session.rollback()
            raise e
        finally:
            self.current_session.close()    

url_repository = UrlService()
