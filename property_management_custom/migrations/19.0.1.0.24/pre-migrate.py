import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Drop the old target_unit_id column (was product.product FK) so the new
    target_property_id column (property.property FK) gets created cleanly."""
    try:
        cr.execute("""
            ALTER TABLE crm_lead
            DROP COLUMN IF EXISTS target_unit_id;
        """)
        _logger.info("Migration 19.0.1.0.24: dropped stale target_unit_id column from crm_lead")
    except Exception as e:
        _logger.warning("Migration 19.0.1.0.24: could not drop target_unit_id: %s", e)
