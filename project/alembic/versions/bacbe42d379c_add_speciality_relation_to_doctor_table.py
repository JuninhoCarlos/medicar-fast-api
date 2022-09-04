"""add speciality relation to doctor table

Revision ID: bacbe42d379c
Revises: 1e2e4218138a
Create Date: 2022-09-03 14:36:38.149187

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "bacbe42d379c"
down_revision = "1e2e4218138a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "especialidade",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nome", sa.String(50), nullable=False),
    )

    op.add_column(
        "doctor",
        sa.Column("especialidade_id", sa.Integer, sa.ForeignKey("especialidade.id")),
    )


def downgrade() -> None:
    op.drop_column("doctor", "especialidade_id")
    op.drop_table("especialidade")
