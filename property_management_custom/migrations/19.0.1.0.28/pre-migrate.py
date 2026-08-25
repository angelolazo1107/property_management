import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Drop stale foreign key constraints and columns on crm_lead and sale_order
    so Odoo creates fresh Many2one FK columns to x_buildings and account.analytic.account."""
    try:
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS target_unit_id CASCADE;")
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS target_property_id CASCADE;")
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS building_id CASCADE;")
        cr.execute("ALTER TABLE sale_order DROP COLUMN IF EXISTS target_unit_id CASCADE;")
        _logger.info("Migration 19.0.1.0.28: dropped stale crm_lead and sale_order columns cleanly")
    except Exception as e:
        _logger.warning("Migration 19.0.1.0.28: error dropping columns: %s", e)
