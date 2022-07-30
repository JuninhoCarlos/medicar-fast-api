"""create a doctor table

Revision ID: 1e2e4218138a
Revises: 
Create Date: 2022-07-30 13:24:38.628153

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1e2e4218138a"
down_revision = None
branch_labels = None
depends_on = None

# id = Column(Integer, primary_key=True)
# name = Column(String(100))
# crm = Column(Integer, unique=True)
# email = Column(Text)


def upgrade() -> None:
    op.create_table(
        "doctor",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("crm", sa.Integer, unique=True),
        sa.Column("email", sa.Text),
    )


def downgrade() -> None:
    op.drop_table("doctor")
