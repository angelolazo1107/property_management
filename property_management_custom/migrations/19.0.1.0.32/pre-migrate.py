import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    try:
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS target_unit_id CASCADE;")
        cr.execute("ALTER TABLE crm_lead DROP COLUMN IF EXISTS building_id CASCADE;")
        _logger.info("Migration 19.0.1.0.32: dropped columns cleanly")
    except Exception as e:
        _logger.warning("Migration 19.0.1.0.32 error: %s", e)
