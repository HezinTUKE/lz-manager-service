from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f8cf7aebfe86"
down_revision: Union[str, None] = "873ad83450bf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Create the Enum type
address_status_enum = sa.Enum("PENDING", "ACCEPTED", "REJECTED", name="addressstatus")

def upgrade() -> None:
    """Upgrade schema."""
    # Create the enum type in the DB
    address_status_enum.create(op.get_bind(), checkfirst=True)

    # Add the column using the enum
    op.add_column("address", sa.Column("status", address_status_enum, nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    # Drop the column first
    op.drop_column("address", "status")

    # Then drop the enum type
    address_status_enum.drop(op.get_bind(), checkfirst=True)
