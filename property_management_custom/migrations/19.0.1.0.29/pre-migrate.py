import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """Clean drop stale FK columns so ORM registers x_buildings and account.analytic.account cleanly."""
    try:
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS target_unit_id CASCADE;")
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS target_property_id CASCADE;")
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS building_id CASCADE;")
        cr.execute("ALTER TABLE sale_order DROP COLUMN IF EXISTS target_unit_id CASCADE;")
        _logger.info("Migration 19.0.1.0.29: cleanly dropped columns")
    except Exception as e:
        _logger.warning("Migration 19.0.1.0.29 error: %s", e)
