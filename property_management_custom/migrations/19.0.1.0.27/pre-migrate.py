import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Drop stale crm_lead columns so the ORM recreates them pointing to
    the correct Studio models (x_buildings, account.analytic.account)."""
    try:
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS target_unit_id;")
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS target_property_id;")
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS building_id;")
        _logger.info("Migration 19.0.1.0.27: dropped stale crm_lead columns for rebuild")
    except Exception as e:
        _logger.warning("Migration 19.0.1.0.27: error during column drop: %s", e)
