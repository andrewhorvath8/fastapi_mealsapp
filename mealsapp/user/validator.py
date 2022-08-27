from typing import Optional

from sqlalchemy.orm import Session

from . import models


# Search and return with user with specific email
async def get_user_by_email(email: str, db_session: Session) -> Optional[models.User]:
    return db_session.query(models.User).filter(models.User.email == email).first()
